from flask import Flask, render_template, request, jsonify
import random
import json
from datetime import datetime

app = Flask(__name__)

# Load cryptocurrency data from JSON file
with open('data.json', 'r') as f:
    CRYPTO_DATA = json.load(f)

def get_sustainable_coins_response():
    sustainable_coins = [(name, data) for name, data in CRYPTO_DATA.items() if data['sustainability_score'] >= 8]
    response = "🌱 Here are the most sustainable cryptocurrencies:\n\n"
    for name, data in sustainable_coins:
        response += f"🌿 **{name} ({data['symbol']})** - Sustainability Score: {data['sustainability_score']}/10\n"
        response += f"   ⚡ Energy Use: {data['energy_use']}\n"
        response += f"   💡 {data['recommendation']}\n\n"
    response += "🌍 These coins use energy-efficient consensus mechanisms and have minimal environmental impact!"
    return response

def get_trending_coins_response():
    rising_coins = [(name, data) for name, data in CRYPTO_DATA.items() if data['price_trend'] == 'rising']
    response = "📈 Currently trending cryptocurrencies:\n\n"
    for name, data in rising_coins:
        response += f"🚀 **{name} ({data['symbol']})** - {data['current_price']}\n"
        response += f"   📊 Market Cap: {data['market_cap']}\n"
        response += f"   🎯 Growth Potential: {data['growth_potential'].replace('_', ' ').title()}\n\n"
    response += "🔥 These coins are showing upward momentum right now!"
    return response

def get_long_term_investment_response():
    response = "🎯 Best long-term investment options:\n\n"
    response += "🏆 **Top Picks for Long-term:**\n"
    response += "1. **Ethereum (ETH)** - Smart contract leader with sustainable upgrade\n"
    response += "2. **Cardano (ADA)** - Academic approach with high sustainability\n"
    response += "3. **Algorand (ALGO)** - Most sustainable with strong tech foundation\n\n"
    response += "💡 **Strategy Tips:**\n"
    response += "• Diversify across different use cases\n"
    response += "• Consider sustainability for future regulations\n"
    response += "• Look for strong development teams and communities\n"
    response += "• Don't invest more than you can afford to lose!"
    return response

def get_market_overview_response():
    response = "💰 Current market overview:\n\n"
    for name, data in list(CRYPTO_DATA.items())[:5]:  # Top 5 by market cap
        trend_emoji = "📈" if data['price_trend'] == 'rising' else "📊" if data['price_trend'] == 'stable' else "📉"
        response += f"{trend_emoji} **{name}**: {data['current_price']} (Market Cap: {data['market_cap']})\n"
    response += "\n💡 Remember: Prices are highly volatile and can change rapidly!"
    return response

def get_greeting_response():
    return ("🚀 Welcome to EzeCrypto! I'm here to help you navigate the crypto universe!\n\n"
            "🤖 **I can help you with:**\n"
            "• 🌱 Sustainable cryptocurrency recommendations\n"
            "• 📈 Trending coins and market analysis\n"
            "• 🎯 Long-term investment strategies\n"
            "• 💰 Current prices and market caps\n"
            "• 📊 Comprehensive crypto summaries\n\n"
            "Just ask me anything about cryptocurrencies!")

INTENTS = {
    get_sustainable_coins_response: ['sustainable', 'eco', 'green', 'environment', 'energy'],
    get_trending_coins_response: ['trending', 'popular', 'hot', 'rising'],
    get_long_term_investment_response: ['long term', 'investment', 'hodl', 'future'],
    get_market_overview_response: ['price', 'cost', 'value', 'market'],
    get_greeting_response: ['hello', 'hi', 'help', 'what can you do']
}

def generate_crypto_response(user_message):
    """Generate contextual responses based on user input"""
    message_lower = user_message.lower()

    for intent_func, keywords in INTENTS.items():
        if any(word in message_lower for word in keywords):
            return intent_func()

    # Default response for unrecognized queries
    responses = [
        "🤔 That's an interesting question! For specific crypto advice, try asking about sustainable coins, trending options, or long-term investments.",
        "🚀 I'd love to help! You can ask me about eco-friendly cryptocurrencies, current trends, or market analysis.",
        "💡 Great question! I specialize in crypto recommendations. Try asking about sustainable investments or trending coins!",
        "🤷‍♂️ I'm not sure about that specific topic, but I can definitely help with cryptocurrency recommendations and market insights!"
    ]
    return random.choice(responses)

def _get_growth_score(potential):
    """Convert growth potential string to a numeric score."""
    if 'very_high' in potential:
        return 3
    if 'high' in potential:
        return 2
    if 'moderate' in potential:
        return 1
    return 0

def generate_full_summary():
    """Generate comprehensive summary of all cryptocurrencies"""
    coins_list = []
    for name, data in CRYPTO_DATA.items():
        coins_list.append({
            "name": name,
            **data
        })

    # Generate statistics
    rising_coins = [coin for coin in coins_list if coin['price_trend'] == 'rising']
    stable_coins = [coin for coin in coins_list if coin['price_trend'] == 'stable']
    eco_friendly = [coin for coin in coins_list if coin['sustainability_score'] >= 8]
    high_growth = [coin for coin in coins_list if 'high' in coin['growth_potential']]

    # Find top picks
    most_sustainable = max(coins_list, key=lambda x: x['sustainability_score'])
    
    # Find the coin with the highest growth potential score
    highest_growth = max(coins_list, key=lambda x: _get_growth_score(x['growth_potential']))

    # Find the best balanced coin (high sustainability + growth)
    # The balanced score is a weighted average of sustainability and growth.
    balanced_scores = []
    for coin in coins_list:
        growth_score = _get_growth_score(coin['growth_potential'])
        # Weighted average: 2 parts growth, 1 part sustainability
        balanced_score = (coin['sustainability_score'] + growth_score * 2) / 3
        balanced_scores.append((coin, balanced_score))

    best_balanced = max(balanced_scores, key=lambda x: x[1])[0]

    return {
        "coins": coins_list,
        "statistics": {
            "rising": {
                "count": len(rising_coins),
                "coins": [coin['symbol'] for coin in rising_coins]
            },
            "stable": {
                "count": len(stable_coins),
                "coins": [coin['symbol'] for coin in stable_coins]
            },
            "eco_friendly": {
                "count": len(eco_friendly),
                "coins": [coin['symbol'] for coin in eco_friendly]
            },
            "high_growth": {
                "count": len(high_growth),
                "coins": [coin['symbol'] for coin in high_growth]
            }
        },
        "top_picks": {
            "most_sustainable": {
                "name": most_sustainable['name'],
                "score": most_sustainable['sustainability_score']
            },
            "highest_growth": {
                "name": highest_growth['name'],
                "potential": highest_growth['growth_potential'].replace('_', ' ').title()
            },
            "best_balanced": {
                "name": best_balanced['name']
            }
        }
    }

@app.route('/')
def index():
    """Serve the main chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({
                'success': False,
                'error': 'No message provided'
            }), 400
        
        user_message = data['message'].strip()
        
        if not user_message:
            return jsonify({
                'success': False,
                'error': 'Empty message'
            }), 400
        
        # Generate response
        bot_response = generate_crypto_response(user_message)
        
        return jsonify({
            'success': True,
            'response': {
                'message': bot_response,
                'type': 'text'
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}'
        }), 500

@app.route('/full_summary')
def full_summary():
    """Generate and return comprehensive crypto summary"""
    try:
        summary_data = generate_full_summary()
        
        return jsonify({
            'success': True,
            'type': 'summary',
            'data': summary_data
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Could not generate summary: {str(e)}'
        }), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'available_coins': len(CRYPTO_DATA)
    })

if __name__ == '__main__':
    print("🚀 Starting EzeCrypto Flask Server...")
    print("📊 Loaded", len(CRYPTO_DATA), "cryptocurrencies")
    print("🌐 Server will be available at http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)