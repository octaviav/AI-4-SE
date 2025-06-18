// DOM Elements
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const chatMessages = document.getElementById('chatMessages');
const typingIndicator = document.getElementById('typingIndicator');
const errorMessage = document.getElementById('errorMessage');

// Quick action handler
function sendQuickMessage(text) {
    messageInput.value = text;
    sendMessage();
}
// full summary handler
async function requestFullSummary() {
    showTyping(true);
    try {
        const response = await fetch('/full_summary');
        const data = await response.json();
        addMessage(data.response, 'bot');
    } catch (error) {
        showError("Couldn't load full summary");
    } finally {
        showTyping(false);
    }
}

// Main message handler
async function sendMessage() {
    const message = messageInput.value.trim();
    if (!message) return;
    
    // Add user message
    addMessage(message, 'user');
    messageInput.value = '';
    showTyping(true);
    
    try {
        // Get bot response
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `message=${encodeURIComponent(message)}`
        });
        
        if (!response.ok) throw new Error('Network response was not ok');
        
        const data = await response.json();
        addMessage(data.response, 'bot');
    } catch (error) {
        showError("Oops! Couldn't connect to the chatbot. Please try again.");
        console.error('Error:', error);
    } finally {
        showTyping(false);
    }
}

// Add message to chat
function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    
    messageDiv.innerHTML = `
        <div class="avatar ${sender}-avatar">${sender === 'bot' ? '🤖' : '👤'}</div>
        <div class="message-content">${formatMessage(text)}</div>
    `;
    
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// line breaks and emoji styling
function formatMessage(text) {
    return text
        .replace(/\n/g, '<br>')
        .replace(/(🚀|📈|🌱|💰|📊|🤖|👥|⚡|🎯)/g, '<span class="emoji">$1</span>');
}

// Typing indicator
function showTyping(show) {
    typingIndicator.style.display = show ? 'flex' : 'none';
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Error display
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
    setTimeout(() => {
        errorMessage.style.display = 'none';
    }, 5000);
}

// Event listeners
sendButton.addEventListener('click', sendMessage);
messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});