# Vim

## Notes

```sh
" use hybrid line numbering by default with automatic toggling
augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
  autocmd BufLeave,FocusLost,InsertEnter   * set norelativenumber
augroup END

" Change directory to the current buffer when opening files.
set autochdir

:%bd|e#  " close all other buffers; reopen last buffer

" Execute bash script; passing CWD to script
function InsertMdLink()
  let l:path = expand('%:p:h')
  execute 'r!vimsert ' . l:path
endfunction
```
