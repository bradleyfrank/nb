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
