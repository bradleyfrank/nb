# Bash

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
