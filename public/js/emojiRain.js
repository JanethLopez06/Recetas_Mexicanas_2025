// emojiRain.js - Lluvia de emojis de cocina 🍳🥄🍅
console.log("emojiRain.js cargado correctamente 🚀");

window.addEventListener("DOMContentLoaded", () => {
  const emojis = ["🥑", "🥬", "🌶", "🥕", "🍏", "🥩", "🍗", "🍅", "🥄"];

  function createEmoji() {
    const emoji = document.createElement("div");
    emoji.innerText = emojis[Math.floor(Math.random() * emojis.length)];
    emoji.style.position = "fixed";
    emoji.style.left = Math.random() * window.innerWidth + "px";
    emoji.style.top = "-40px";
    emoji.style.fontSize = 20 + Math.random() * 20 + "px";
    emoji.style.zIndex = 9999;
    emoji.style.pointerEvents = "none";
    emoji.style.opacity = 0.9;
    emoji.style.transition = `top ${4 + Math.random() * 3}s linear`;

    document.body.appendChild(emoji);

    // Inicia animación
    setTimeout(() => {
      emoji.style.top = window.innerHeight + "px";
    }, 10);

    // Elimina después de caer
    setTimeout(() => {
      if (emoji && emoji.parentNode) {
        emoji.parentNode.removeChild(emoji);
      }
    }, 7000);
  }

  // Crear un emoji nuevo cada 300ms
  setInterval(createEmoji, 300);
});
