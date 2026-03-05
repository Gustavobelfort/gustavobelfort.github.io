var CONFIG = CONFIG || {};

CONFIG.prompt = function(cwd, user) {
   if (user)
      return '<span class="user">' + user +
          '</span>@<span class="host">belfort.dev</span>:<span class="cwd">' +
          cwd + '</span>$ ';
   return '-bash $ ';
};

CONFIG.username = '';
