document.addEventListener("DOMContentLoaded", function () {
    const messages = document.querySelectorAll(".message");
    

    messages.forEach(message => {
        setTimeout(() => {
            message.classList.add("fade-out");

            setTimeout(() => {
                message.remove();
            }, 500); // Espera a que termine la transición antes de eliminarlo
        }, 3000); // 3 segundos antes de desaparecer
    });

});