        const messageInput = document.getElementById('messageInput');
        const sendButton = document.getElementById('sendButton');
        const chatMessages = document.getElementById('chatMessages');
        const typingIndicator = document.getElementById('typingIndicator');
        const errorMessage = document.getElementById('errorMessage');
        const chatForm = document.getElementById('chatForm');

        // Initialize chat
        document.addEventListener('DOMContentLoaded', function() {
            // Add welcome message
            addMessage("Hey there! 🚀 Ready to explore the crypto universe? Ask me about trending coins, sustainable investments, or request a full summary!", 'bot');
        });

        // Quick action handler
        function sendQuickMessage(text) {
            messageInput.value = text;
            sendMessage();
        }

        // Full summary handler
        async function requestFullSummary() {
            showTyping(true);
            try {
                const response = await fetch('/full_summary');
                const data = await response.json();
                
                if (data.success) {
                    if (data.type === 'summary' && data.data) {
                        displaySummary(data.data);
                    } else {
                        addMessage(data.response, 'bot');
                    }
                } else {
                    showError(data.error || "Couldn't load full summary");
                }
            } catch (error) {
                showError("Couldn't connect to get full summary");
                console.error('Error:', error);
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
            sendButton.disabled = true;
            
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
                
                if (data.success) {
                    if (data.type === 'summary' && data.data) {
                        displaySummary(data.data);
                    } else {
                        addMessage(data.response, 'bot');
                    }
                } else {
                    showError(data.error || "Something went wrong");
                }
            } catch (error) {
                showError("Oops! Couldn't connect to the chatbot. Please try again.");
                console.error('Error:', error);
            } finally {
                showTyping(false);
                sendButton.disabled = false;
            }
        }

        // Display comprehensive summary
        function displaySummary(summaryData) {
            let summaryHtml = '<div class="summary-card"><h3>📊 Comprehensive Crypto Summary</h3>';
            
            // Add coins
            summaryData.coins.forEach((coin, index) => {
                const trendEmoji = coin.price_trend === 'rising' ? '📈' : coin.price_trend === 'stable' ? '📊' : '📉';
                const sustainabilityBar = '█'.repeat(coin.sustainability_score) + '░'.repeat(10 - coin.sustainability_score);
                const sustainabilityEmoji = coin.sustainability_score >= 8 ? '🌱' : coin.sustainability_score >= 6 ? '🟢' : coin.sustainability_score >= 4 ? '🟡' : '🔴';
                
                summaryHtml += `
                    <div class="coin-item">
                        <div class="coin-header">${index + 1}. ${coin.name} (${coin.symbol})</div>
                        <div class="coin-details">
                            💰 Price: ${coin.current_price} ${trendEmoji} ${coin.price_trend}<br>
                            🏢 Market Cap: ${coin.market_cap} | 📊 Volatility: ${coin.volatility}<br>
                            👥 Adoption: ${coin.adoption} | 🚀 Growth: ${coin.growth_potential.replace('_', ' ')}<br>
                            ${sustainabilityEmoji} Sustainability: ${coin.sustainability_score}/10 [${sustainabilityBar}]<br>
                            ⚡ Energy Use: ${coin.energy_use}<br>
                            💡 ${coin.recommendation}
                        </div>
                    </div>
                `;
            });
            
            // Add statistics
            summaryHtml += `
                <div style="margin-top: 20px; padding: 15px; background: white; border-radius: 8px;">
                    <h4>📈 Market Overview</h4>
                    <p>📈 Rising: ${summaryData.statistics.rising.count} coins (${summaryData.statistics.rising.coins.join(', ')})</p>
                    <p>📊 Stable: ${summaryData.statistics.stable.count} coins (${summaryData.statistics.stable.coins.join(', ')})</p>
                    <p>🌱 Eco-Friendly: ${summaryData.statistics.eco_friendly.count} coins (${summaryData.statistics.eco_friendly.coins.join(', ')})</p>
                    <p>🚀 High Growth: ${summaryData.statistics.high_growth.count} coins (${summaryData.statistics.high_growth.coins.join(', ')})</p>
                </div>
            `;
            
            // Add top picks
            summaryHtml += `
                <div style="margin-top: 15px; padding: 15px; background: white; border-radius: 8px;">
                    <h4>🏆 Top Picks</h4>
                    <p>🌱 Most Sustainable: ${summaryData.top_picks.most_sustainable.name} (${summaryData.top_picks.most_sustainable.score}/10)</p>
                    <p>🚀 Highest Growth: ${summaryData.top_picks.highest_growth.name} (${summaryData.top_picks.highest_growth.potential})</p>
                    <p>⚖️ Best Balanced: ${summaryData.top_picks.best_balanced.name}</p>
                </div>
            `;
            
            summaryHtml += '</div>';
            
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message bot';
            messageDiv.innerHTML = `
                <div class="avatar bot-avatar">🤖</div>
                <div class="message-content">${summaryHtml}</div>
            `;
            
            chatMessages.appendChild(messageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
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

        // Format message with line breaks and emoji styling
        function formatMessage(text) {
            return text
                .replace(/\n/g, '<br>')
                .replace(/(🚀|📈|🌱|💰|📊|🤖|👥|⚡|🎯|🔥|🤔|🤷‍♂️|💡|🏆|🟢|🟡|🔴|⚖️|👍|🌿)/g, '<span class="emoji">$1</span>');
        }

        // Typing indicator
        function showTyping(show) {
            typingIndicator.style.display = show ? 'flex' : 'none';
            if (show) {
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }
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
        chatForm.addEventListener('submit', function(e) {
            e.preventDefault();
            sendMessage();
        });

        messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });

        // Auto-focus input
        messageInput.focus();