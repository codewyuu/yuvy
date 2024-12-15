document.getElementById("add-password-form").addEventListener("submit", function(event) {
    event.preventDefault();
    let website = document.getElementById("website").value;
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    // Here you would send the data to your Python backend using fetch or an AJAX request.
    console.log("Password added:", website, username, password);
    alert("Password successfully added!");
    document.getElementById("add-password-form").reset();
});

document.getElementById("get-password-form").addEventListener("submit", function(event) {
    event.preventDefault();
    let website = document.getElementById("retrieve-website").value;

    // This is where you would request the password from your backend
    console.log("Retrieving password for:", website);

    // Simulate retrieved password for demonstration
    let passwordResult = document.getElementById("password-result");
    passwordResult.innerHTML = `
        <p>Website: ${website}</p>
        <p>Username: user1</p>
        <p>Password: secret123</p>
    `;
});