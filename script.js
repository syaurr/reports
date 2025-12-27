document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    const colors = ['pink', 'orange', 'green', 'neon'];
    const bubbleCount = 15; // Tambah jumlah biar lebih ramai

    for (let i = 0; i < bubbleCount; i++) {
        const bubble = document.createElement('div');
        
        // Pilih warna acak dari list
        const colorClass = colors[Math.floor(Math.random() * colors.length)];
        bubble.classList.add('bubble', colorClass);
        
        // Ukuran acak
        const size = Math.random() * 50 + 20 + "px";
        bubble.style.width = size;
        bubble.style.height = size;
        
        // Posisi horizontal acak (0 sampai 100% lebar layar)
        bubble.style.left = Math.random() * 100 + "vw";
        
        // Kecepatan meluncur acak
        const duration = Math.random() * 8 + 7 + "s";
        bubble.style.animationDuration = duration;
        
        // Waktu tunggu acak biar tidak barengan munculnya
        bubble.style.animationDelay = Math.random() * 10 + "s";
        
        body.appendChild(bubble);
    }

    console.log("Bubbles initialized!"); // Cek di Inspect Element > Console
});