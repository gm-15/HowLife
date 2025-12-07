importScripts("https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js");
importScripts("https://www.gstatic.com/firebasejs/10.8.0/firebase-messaging.js");

firebase.initializeApp({
  apiKey: "YOUR_KEY",
  authDomain: "YOUR_DOMAIN",
  projectId: "YOUR_PROJECT",
  messagingSenderId: "YOUR_MSG_ID",
  appId: "YOUR_ID"
});

const messaging = firebase.messaging();

messaging.onBackgroundMessage((payload) => {
  console.log("Background message received", payload);

  self.registration.showNotification(payload.notification.title, {
    body: payload.notification.body,
    icon: "/logo.png"
  });
});
