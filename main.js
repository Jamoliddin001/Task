if (window.Telegram && window.Telegram.WebApp) {
    window.Telegram.WebApp.init();
    console.log("Telegram WebApp инициализирован.");
} else {
    console.log("Запуск не внутри Telegram.");
}