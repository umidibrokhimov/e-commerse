let form = document.querySelector('#contact');

form.addEventListener('submit', (e)=> {
    e.preventDefault()
    
    username = form.querySelector('#name').value
    email = form.querySelector('#email').value
    subject = form.querySelector('#subject').value
    message = form.querySelector('#message').value
    
    let my_text = `New user is: %0A - Name: ${username} %0A - UserEmail is: ${email} %0A - UserSubject is: ${subject} %0A - Message is: ${message}`
    
    let token = '5364201856:AAG9P3GruT17uqf0YEOsCC52vI1SapIuwSo';
    let chat_id = -1001640322912
    
    let url = `https://api.telegram.org/bot${token}/sendMessage?chat_id=${chat_id}&text=${my_text}`
    
    let api = new XMLHttpRequest()
    api.open("GET", url, true)
    api.send()
    console.log("Ishlamoqda!")
})