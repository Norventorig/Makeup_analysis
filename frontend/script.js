document.getElementById('uploadBtn').addEventListener('click', async () => {
    const input = document.getElementById('imageInput');
    if (!input.files.length) {
        alert('Выберите изображение!');
        return;
    }

    const file = input.files[0];
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('http://127.0.0.1:8000/predict/', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Ошибка сервера');
        }

        const data = await response.json();
        document.getElementById('result').textContent = 'Prediction: ' + data.prediction;
    } catch (error) {
        document.getElementById('result').textContent = 'Ошибка: ' + error.message;
    }
});
