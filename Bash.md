# Bash

## Tags

## Notes

                        +-------+-------+-----------+
                VAR is: | unset | empty | non-empty |
+-----------------------+-------+-------+-----------+
| [ -z "${VAR}" ]       | true  | true  | false     |
| [ -z "${VAR+set}" ]   | true  | false | false     |
| [ -z "${VAR-unset}" ] | false | true  | false     |
| [ -n "${VAR}" ]       | false | false | true      |
| [ -n "${VAR+set}" ]   | false | true  | true      |
| [ -n "${VAR-unset}" ] | true  | false | true      |
+-----------------------+-------+-------+-----------+

```sh
cat << EOF > /path/to/file  # variables will be interpreted
cat << 'EOF' > /path/to/file  # variables will not be interpreted
cat << 'EOF' | sed 's/foo/bar/g' > /path/to/file  # replace 'foo' with 'bar'
cat << 'EOF' | sudo tee /path/to/file  # write to file using sudo

read -rsp "Enter password: " my_password  # enter a password securely

# read file into array (Bash 4+)
mapfile -t foo < "file"
readarray -t foo < <( find . -name * )

# substrings: ${<var>:<start>} or ${<var>:<start>:<length>}
foo="substring example"
echo ${foo:5:5}  # ring
echo ${foo:3}    # string example
echo ${foo:0:-3} # substring exam

bar="path1/path2/file.ext"
echo "${bar#*.}"   # ext
echo "${bar##*/}"  # file.ext
echo "${bar%/*}"   # path1/path2
echo "${bar%%/*}"  # path1
```

### Zsh

```sh
setopt transient_rprompt  # show zsh right prompt only on active prompt
%(5~|%-1~/.../%3~|%~)  # truncate to 1st and last 3 segments if longer than 5
```
