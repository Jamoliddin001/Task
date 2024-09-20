window.Telegram.WebApp.init();

window.Telegram.WebApp.onEvent('web_app_close', function() {
    console.log('Mini App Closed');
});

const user = window.Telegram.WebApp.initDataUnsafe.user;
console.log("User ID:", user.id);
