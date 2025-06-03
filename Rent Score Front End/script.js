// Function to update the score and rotate the needle
function updateScoreFromBackend() {
    // Make a GET request to the backend endpoint that provides the score
    fetch('/getScore') // Update the URL to your backend endpoint
      .then(response => response.json())
      .then(data => {
        const score = data.score; // Assuming the response contains the score
        // Set the --score variable in CSS
        needle.style.setProperty('--score', score);
        // Update the displayed score
        document.querySelector('.score').textContent = score;
      })
      .catch(error => {
        console.error('Error fetching score:', error);
      });
  }
  
  // Call the function initially to fetch and update the score
  updateScoreFromBackend();
  
  // Example: Call the function periodically to update the score (every 5 seconds)
  setInterval(updateScoreFromBackend, 5000);
  