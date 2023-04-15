(global-linum-mode t)
(setq c-default-style "bsd"
      c-basic-offset 8
      tab-width 8
      indent-tabs-mode t)
(require 'whitespace)
(setq whitespace-style '(face empty lines-tail trailing))
(global-whitespace-mode t)
(setq column-number-mode t)
(defun my-js-mode-hook ()
  (setq-local tab-width 1)
  (setq-local indent-tabs-mode nil))

(add-hook 'js-mode-hook 'my-js-mode-hook)
