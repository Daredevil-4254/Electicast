function toggleNav() {
    var navLinks = document.querySelector('.nav-links');
    var burger = document.querySelector('.burger');
    navLinks.classList.toggle('active');
    burger.classList.toggle('toggle');
  }
  
  function validateForm() {
    var nameInput = document.getElementById('name');
    var emailInput = document.getElementById('email');
    var messageInput = document.getElementById('message');
  
    if (nameInput.value === '') {
      alert('Please enter your name.');
      return false;
    }
  
    if (emailInput.value === '') {
      alert('Please enter your email.');
      return false;
    }
  
    if (messageInput.value === '') {
      alert('Please enter your message.');
      return false;
    }
  
    alert('Message sent successfully!');
    document.getElementById('contact-form').reset();
  }
  