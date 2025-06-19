from flask import Flask, render_template_string, request, jsonify
import random
import json
from datetime import datetime

app = Flask(__name__)

# Sample cryptocurrency data for demonstration
CRYPTO_DATA = {
    "Bitcoin": {
        "symbol": "BTC",
        "current_price": "$43,250",
        "market_cap": "$847B",
        "price_trend": "rising",
        "volatility": "Medium",
        "adoption": "Very High",
        "growth_potential": "moderate_growth",
        "sustainability_score": 3,
        "energy_use": "Very High",
        "recommendation": "Strong store of value but high energy consumption"
    },
    "Ethereum": {
        "symbol": "ETH",
        "current_price": "$2,650",
        "market_cap": "$318B",
        "price_trend": "stable",
        "volatility": "Medium",
        "adoption": "Very High",
        "growth_potential": "high_growth",
        "sustainability_score": 8,
        "energy_use": "Low (after merge)",
        "recommendation": "Excellent for DeFi and smart contracts with improved sustainability"
    },
    "Cardano": {
        "symbol": "ADA",
        "current_price": "$0.48",
        "market_cap": "$17B",
        "price_trend": "rising",
        "volatility": "High",
        "adoption": "Medium",
        "growth_potential": "high_growth",
        "sustainability_score": 9,
        "energy_use": "Very Low",
        "recommendation": "Great sustainable choice with strong academic foundation"
    },
    "Solana": {
        "symbol": "SOL",
        "current_price": "$98",
        "market_cap": "$43B",
        "price_trend": "rising",
        "volatility": "High",
        "adoption": "High",
        "growth_potential": "very_high_growth",
        "sustainability_score": 7,
        "energy_use": "Low",
        "recommendation": "Fast and efficient but still developing ecosystem"
    },
    "Polkadot": {
        "symbol": "DOT",
        "current_price": "$7.20",
        "market_cap": "$9B",
        "price_trend": "stable",
        "volatility": "High",
        "adoption": "Medium",
        "growth_potential": "high_growth",
        "sustainability_score": 8,
        "energy_use": "Low",
        "recommendation": "Innovative interoperability solution with good sustainability"
    },
    "Algorand": {
        "symbol": "ALGO",
        "current_price": "$0.19",
        "market_cap": "$1.5B",
        "price_trend": "stable",
        "volatility": "Medium",
        "adoption": "Low",
        "growth_potential": "high_growth",
        "sustainability_score": 10,
        "energy_use": "Carbon Negative",
        "recommendation": "Most sustainable option with strong technology foundation"
    },
    "Tezos": {
        "symbol": "XTZ",
        "current_price": "$1.02",
        "market_cap": "$950M",
        "price_trend": "declining",
        "volatility": "High",
        "adoption": "Low",
        "growth_potential": "moderate_growth",
        "sustainability_score": 9,
        "energy_use": "Very Low",
        "recommendation": "Sustainable and self-upgrading but needs more adoption"
    },
    "Chainlink": {
        "symbol": "LINK",
        "current_price": "$14.80",
        "market_cap": "$8.2B",
        "price_trend": "rising",
        "volatility": "High",
        "adoption": "High",
        "growth_potential": "high_growth",
        "sustainability_score": 6,
        "energy_use": "Medium",
        "recommendation": "Essential oracle infrastructure with growing demand"
    }
}

def generate_crypto_response(user_message):
    """Generate contextual responses based on user input"""
    message_lower = user_message.lower()
    
    # Eco-friendly/Sustainable queries
    if any(word in message_lower for word in ['sustainable', 'eco', 'green', 'environment', 'energy']):
        sustainable_coins = [(name, data) for name, data in CRYPTO_DATA.items() if data['sustainability_score'] >= 8]
        response = "🌱 Here are the most sustainable cryptocurrencies:\n\n"
        for name, data in sustainable_coins:
            response += f"🌿 **{name} ({data['symbol']})** - Sustainability Score: {data['sustainability_score']}/10\n"
            response += f"   ⚡ Energy Use: {data['energy_use']}\n"
            response += f"   💡 {data['recommendation']}\n\n"
        response += "🌍 These coins use energy-efficient consensus mechanisms and have minimal environmental impact!"
        return response
    
    # Trending/Popular queries
    elif any(word in message_lower for word in ['trending', 'popular', 'hot', 'rising']):
        rising_coins = [(name, data) for name, data in CRYPTO_DATA.items() if data['price_trend'] == 'rising']
        response = "📈 Currently trending cryptocurrencies:\n\n"
        for name, data in rising_coins:
            response += f"🚀 **{name} ({data['symbol']})** - {data['current_price']}\n"
            response += f"   📊 Market Cap: {data['market_cap']}\n"
            response += f"   🎯 Growth Potential: {data['growth_potential'].replace('_', ' ').title()}\n\n"
        response += "🔥 These coins are showing upward momentum right now!"
        return response
    
    # Long-term investment queries
    elif any(word in message_lower for word in ['long term', 'investment', 'hodl', 'future']):
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
    
    # Price/Market queries
    elif any(word in message_lower for word in ['price', 'cost', 'value', 'market']):
        response = "💰 Current market overview:\n\n"
        for name, data in list(CRYPTO_DATA.items())[:5]:  # Top 5 by market cap
            trend_emoji = "📈" if data['price_trend'] == 'rising' else "📊" if data['price_trend'] == 'stable' else "📉"
            response += f"{trend_emoji} **{name}**: {data['current_price']} (Market Cap: {data['market_cap']})\n"
        response += "\n💡 Remember: Prices are highly volatile and can change rapidly!"
        return response
    
    # General help or greeting
    elif any(word in message_lower for word in ['hello', 'hi', 'help', 'what can you do']):
        return ("🚀 Welcome to EzeCrypto! I'm here to help you navigate the crypto universe!\n\n"
                "🤖 **I can help you with:**\n"
                "• 🌱 Sustainable cryptocurrency recommendations\n"
                "• 📈 Trending coins and market analysis\n"
                "• 🎯 Long-term investment strategies\n"
                "• 💰 Current prices and market caps\n"
                "• 📊 Comprehensive crypto summaries\n\n"
                "Just ask me anything about cryptocurrencies!")
    
    # Default response for unrecognized queries
    else:
        responses = [
            "🤔 That's an interesting question! For specific crypto advice, try asking about sustainable coins, trending options, or long-term investments.",
            "🚀 I'd love to help! You can ask me about eco-friendly cryptocurrencies, current trends, or market analysis.",
            "💡 Great question! I specialize in crypto recommendations. Try asking about sustainable investments or trending coins!",
            "🤷‍♂️ I'm not sure about that specific topic, but I can definitely help with cryptocurrency recommendations and market insights!"
        ]
        return random.choice(responses)

def generate_full_summary():
    """Generate comprehensive summary of all cryptocurrencies"""
    coins_list = []
    for name, data in CRYPTO_DATA.items():
        coins_list.append({
            "name": name,
            "symbol": data["symbol"],
            "current_price": data["current_price"],
            "market_cap": data["market_cap"],
            "price_trend": data["price_trend"],
            "volatility": data["volatility"],
            "adoption": data["adoption"],
            "growth_potential": data["growth_potential"],
            "sustainability_score": data["sustainability_score"],
            "energy_use": data["energy_use"],
            "recommendation": data["recommendation"]
        })
    
    # Generate statistics
    rising_coins = [coin for coin in coins_list if coin['price_trend'] == 'rising']
    stable_coins = [coin for coin in coins_list if coin['price_trend'] == 'stable']
    eco_friendly = [coin for coin in coins_list if coin['sustainability_score'] >= 8]
    high_growth = [coin for coin in coins_list if 'high' in coin['growth_potential']]
    
    # Find top picks
    most_sustainable = max(coins_list, key=lambda x: x['sustainability_score'])
    highest_growth = max(coins_list, key=lambda x: 3 if 'very_high' in x['growth_potential'] else 2 if 'high' in x['growth_potential'] else 1)
    
    # Best balanced (high sustainability + growth)
    balanced_scores = []
    for coin in coins_list:
        growth_score = 3 if 'very_high' in coin['growth_potential'] else 2 if 'high' in coin['growth_potential'] else 1
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
    try:
        # Read the HTML file from the uploaded document
        with open('paste.txt', 'r', encoding='utf-8') as f:
            html_content = f.read()
        return html_content
    except FileNotFoundError:
        # Fallback minimal HTML if file not found
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>EzeCrypto</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .container { max-width: 800px; margin: 0 auto; }
                .error { color: red; padding: 20px; background: #ffe6e6; border-radius: 5px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 EzeCrypto</h1>
                <div class="error">
                    <p>Chat interface file not found. Please ensure 'paste.txt' is in the same directory as this Flask app.</p>
                    <p>You can still test the API endpoints:</p>
                    <ul>
                        <li>POST /chat - Send messages</li>
                        <li>GET /full_summary - Get comprehensive summary</li>
                    </ul>
                </div>
            </div>
        </body>
        </html>
        """

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