const target = new URL('/invite', 'https://app.froggybot.com');
target.search = window.location.search;
document.querySelector('[data-invite-link]').href = target.toString();
window.location.replace(target.toString());
