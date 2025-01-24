# Ansible

## Tags

#ansible

## Notes

```sh
# encrypt file with existing password
ansible-vault encrypt --vault-id /path/to/password <file>
ansible-vault encrypt_string --stdin-name <variable_name>
```

Test if package is installed:

```yaml
- name: "Confirm 1Password-cli is installed"
  block:
    - name: "Check Homebrew for 1Password-cli"
      ansible.builtin.command:
        cmd: "brew info 1password-cli --json=v2"
      register: cmd_brew_info
      changed_when: false
      when: ansible_facts['system'] == "Darwin"
    - name: "Gather package facts"
      ansible.builtin.package_facts:
        manager: auto
      when: ansible_facts['system'] == "Linux"
    - name: "End if 1Password-cli not installed"
      vars:
        brew_info: "{{ cmd_brew_info['stdout'] | default('{}') | from_json }}"
        pkgs_info: "{{ ansible_facts['packages'] | default({}) }}"
      ansible.builtin.meta: "end_play"
      # TODO: package name changes per distro
      when: "('1password-cli' not in pkgs_info) and
             (brew_info['casks'][0]['installed'] | default('null') == 'null')"
```

Use `dockutil` to configure Dock:

```yaml
- name: "Set MacOS dock apps"
  vars:
    is_spacer: "{{ item['item'] | lower in dock_dockutil_spacers }}"
    f_add: "--add \"{{ '' if is_spacer else item['item'] }}\""
    f_type: "{{ '--type ' + item['item'] | lower if is_spacer else '' }}"
    f_section: "--section {{ item['section'] | default('apps') }}"
    f_position: "--position {{ ansible_loop['index'] }}"
  ansible.builtin.command:
    cmd: "dockutil {{ f_add }} {{ f_type }} {{ f_position }} {{ f_section }} --no-restart"
  loop: "{{ dock_macos_items }}"
  loop_control:
    extended: true
  notify: "Restart macOS dock"
  tags: [dock]
```

```
desktop_dockutil_spacers:
  - "spacer"
  - "small-spacer"
  - "flex-spacer"
```

Import secrets into 1Password:

```yaml
- name: "Set 1Password-cli binary to use session token"
  vars:
    op_account_list: "{{ cmd_op_account_list['stdout'] | from_json }}"
    op_session_env: "OP_SESSION_{{ op_account_list[0]['user_uuid'] }}"
    op_session_token: "{{ cmd_op_signin['stdout_lines'][1] }}"
  ansible.builtin.set_fact:
    op_bin: "{{ op_session_env }}={{ op_session_token }} op"
  tags: [onepassword, auth]

- name: "Retrieve Vault password from file"
  ansible.builtin.set_fact:
    # ignoring errors results in a blank string, which is the desired result
    vault_password: "{{ lookup('ansible.builtin.file', onepassword_ansible_vault, errors='ignore') }}"
  tags: [onepassword, import]

- name: "Add Vault password to secrets list"
  ansible.builtin.set_fact:
    vault_secrets: "{{ vault_secrets | ansible.builtin.combine({'vault_password': vault_password}) }}"
  tags: [onepassword, import]

- name: "Get 1Password Vault id"  # noqa command-instead-of-shell
  ansible.builtin.shell:
    cmd: "{{ op_bin }} vault get '{{ op_vault }}' --format=json"
  changed_when: false
  register: cmd_op_vault_get
  tags: [onepassword, import]

- name: "Output decrypted secrets to template"
  vars:
    vault_id: "{{ cmd_op_vault_get['stdout'] | community.general.json_query('id') }}"
  ansible.builtin.template:
    src: "op.json.j2"
    dest: "{{ op_template }}"
    mode: "0600"
  tags: [onepassword, import]

- name: "Import secrets into 1Password"
  tags: [onepassword, import]
  block:
    - name: "Import secrets into 1Password"
      ansible.builtin.shell:
        # https://1password.community/discussion/comment/703328/#Comment_703328
        cmd: "{{ op_bin }} item create --template {{ op_template }} </dev/null"
      changed_when: false
  always:
    - name: "Remove 1Password template"
      ansible.builtin.file:
        path: "{{ op_template }}"
        state: "absent"
```

Start an SSH Agent and add encrypted keys:

```yaml
- name: "Start ssh-agent"
  ansible.builtin.shell:
    cmd: |
      eval $(ssh-agent -s) > /dev/null
      echo "{\"SSH_AUTH_SOCK\":\"$SSH_AUTH_SOCK\",\"SSH_AGENT_PID\":\"$SSH_AGENT_PID\"}"
  register: cmd_eval_ssh_agent
  changed_when: true
  notify: "Stop ssh-agent"

- name: "Add key to ssh-agent"
  environment: "{{ cmd_eval_ssh_agent['stdout'] }}"
  ansible.builtin.expect:
    command: "ssh-add {{ git_ssh_key_private }}"
    responses:
      passphrase: "{{ git_ssh_key_passphrase }}"

# retrieve agent
...
  vars:
    git_ssh_auth_sock: "{{ cmd_eval_ssh_agent['stdout'] | from_json | json_query('SSH_AUTH_SOCK') }}"
...

# Handler
- name: "Stop ssh-agent"
  ansible.builtin.command:
    cmd: "ssh-agent -k"
  environment:
    SSH_AGENT_PID: "{{ cmd_eval_ssh_agent['stdout'] | from_json | json_query('SSH_AGENT_PID') }}"
  changed_when: false
```

Find and print variables, dynamically:

```yaml
    - name: "Echo vars to force auth to 1Password"
      ansible.builtin.debug:
        msg: "{{ lookup('ansible.builtin.vars', item) }}"
      loop: "{{ query('ansible.builtin.varnames', '^op_.+$') }}"
      no_log: true
```
