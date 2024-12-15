document.getElementById("add-password-form").addEventListener("submit", function(event) {
    event.preventDefault();
    let website = document.getElementById("website").value;
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    fetch('/add-password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            website: website,
            username: username,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        document.getElementById("add-password-form").reset();
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById("get-password-form").addEventListener("submit", function(event) {
    event.preventDefault();
    let website = document.getElementById("retrieve-website").value;

    fetch(`/get-password?website=${encodeURIComponent(website)}`)
    .then(response => response.json())
    .then(data => {
        if (data.password) {
            let passwordResult = document.getElementById("password-result");
            passwordResult.innerHTML = `
                <p>Website: ${data.website}</p>
                <p>Username: ${data.username}</p>
                <p>Password: ${data.password}</p>
            `;
        } else {
            alert(data.message);
        }
    })
    .catch(error => console.error('Error:', error));
});