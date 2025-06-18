from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__, static_folder='static')

class EzeCrypto:
    def __init__(self):
        self.name = "EzeCrypto"
        self.crypto_db = {
            "Bitcoin": {
                "symbol": "BTC",
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3,
                "volatility": "medium",
                "adoption": "high",
                "current_price": "$67,500",
                "growth_potential": "moderate"
            },
            "Ethereum": {
                "symbol": "ETH", 
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6,
                "volatility": "medium",
                "adoption": "high",
                "current_price": "$3,200",
                "growth_potential": "high"
            },
            "Cardano": {
                "symbol": "ADA",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8,
                "volatility": "high",
                "adoption": "medium",
                "current_price": "$0.85",
                "growth_potential": "high"
            },
            "Solana": {
                "symbol": "SOL",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7,
                "volatility": "high",
                "adoption": "medium",
                "current_price": "$145",
                "growth_potential": "very_high"
            },
            "Polygon": {
                "symbol": "MATIC",
                "price_trend": "stable",
                "market_cap": "medium",
                "energy_use": "very_low",
                "sustainability_score": 9,
                "volatility": "high",
                "adoption": "medium",
                "current_price": "$0.92",
                "growth_potential": "high"
            },
            "Chainlink": {
                "symbol": "LINK",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7,
                "volatility": "medium",
                "adoption": "high",
                "current_price": "$18.50",
                "growth_potential": "high"
            }
        }
        
        self.greetings = [
            "Hey there! 🚀 Ready to explore the crypto universe?",
        ]
        
        self.disclaimers = [
            "⚠️  Remember: Crypto is risky—always do your own research!",
        ]

    def greet(self):
        """Welcome message for the chatbot"""
        print("=" * 60)
        print(f"🤖 Welcome to {self.name}! Your Crypto Recommendation Assistant")
        print("=" * 60)
        print(random.choice(self.greetings))
        print("\nYou can ask me about:")
        print("• Trending cryptocurrencies")
        print("• Sustainable/eco-friendly coins")
        print("• High-growth potential investments")
        print("• Specific coin information")
        print("• Investment advice based on your preferences")
        print("• Detailed summary of all cryptocurrencies")
        print("\nType 'quit' or 'exit' to end our chat.")
        print("-" * 60)

    def display_detailed_summary(self):
        """Display a comprehensive summary of all cryptocurrencies"""
        print("\n" + "=" * 80)
        print("📊 DETAILED CRYPTOCURRENCY SUMMARY")
        print("=" * 80)
        
        # Sort coins by market cap and price for better presentation
        sorted_coins = []
        for coin, data in self.crypto_db.items():
            # Convert price to float 
            price_str = data["current_price"].replace("$", "").replace(",", "")
            try:
                price_value = float(price_str)
            except:
                price_value = 0
            sorted_coins.append((coin, data, price_value))
        
        # Sort by price (highest first)
        sorted_coins.sort(key=lambda x: x[2], reverse=True)
        
        for i, (coin, data, _) in enumerate(sorted_coins, 1):
            print(f"\n{i}. {coin} ({data['symbol']})")
            print("-" * 50)
            
            # Price and trend
            trend_emoji = "📈" if data['price_trend'] == 'rising' else "📊" if data['price_trend'] == 'stable' else "📉"
            print(f"   💰 Current Price: {data['current_price']}")
            print(f"   {trend_emoji} Price Trend: {data['price_trend'].title()}")
            
            # Market metric
            print(f"   🏢 Market Cap: {data['market_cap'].title()}")
            print(f"   📊 Volatility: {data['volatility'].title()}")
            print(f"   👥 Adoption: {data['adoption'].title()}")
            
            # Growth and sustanability
            growth_emoji = "🚀" if data['growth_potential'] == 'very_high' else "📈" if data['growth_potential'] == 'high' else "📊"
            print(f"   {growth_emoji} Growth Potential: {data['growth_potential'].replace('_', ' ').title()}")
            
            # Sustainability score with visual indicator
            sustainability_emoji = "🌱" if data['sustainability_score'] >= 8 else "🟢" if data['sustainability_score'] >= 6 else "🟡" if data['sustainability_score'] >= 4 else "🔴"
            sustainability_bars = "█" * data['sustainability_score'] + "░" * (10 - data['sustainability_score'])
            print(f"   {sustainability_emoji} Sustainability: {data['sustainability_score']}/10 [{sustainability_bars}]")
            print(f"   ⚡ Energy Use: {data['energy_use'].replace('_', ' ').title()}")
            
            # Quick recommendation
            if data['sustainability_score'] >= 8:
                print(f"   💡 Recommendation: Excellent eco-friendly choice! 🌿")
            elif data['growth_potential'] == 'very_high':
                print(f"   💡 Recommendation: High growth potential! 🚀")
            elif data['price_trend'] == 'rising' and data['adoption'] == 'high':
                print(f"   💡 Recommendation: Strong momentum with good adoption! 📈")
            elif data['volatility'] == 'medium' and data['adoption'] == 'high':
                print(f"   💡 Recommendation: Stable choice with good market presence! 👍")
        
        # Summary statistics
        print("\n" + "=" * 80)
        print("📈 MARKET OVERVIEW")
        print("=" * 80)
        
        # Calculate statistics
        rising_coins = [coin for coin, data in self.crypto_db.items() if data['price_trend'] == 'rising']
        stable_coins = [coin for coin, data in self.crypto_db.items() if data['price_trend'] == 'stable']
        eco_friendly = [coin for coin, data in self.crypto_db.items() if data['sustainability_score'] >= 7]
        high_growth = [coin for coin, data in self.crypto_db.items() if data['growth_potential'] in ['high', 'very_high']]
        high_adoption = [coin for coin, data in self.crypto_db.items() if data['adoption'] == 'high']
        
        print(f"📈 Rising Trend: {len(rising_coins)} coins ({', '.join(rising_coins)})")
        print(f"📊 Stable Trend: {len(stable_coins)} coins ({', '.join(stable_coins)})")
        print(f"🌱 Eco-Friendly (7+ score): {len(eco_friendly)} coins ({', '.join(eco_friendly)})")
        print(f"🚀 High Growth Potential: {len(high_growth)} coins ({', '.join(high_growth)})")
        print(f"👥 High Adoption: {len(high_adoption)} coins ({', '.join(high_adoption)})")
        
        # Best picks by category
        print(f"\n🏆 TOP PICKS BY CATEGORY:")
        print("-" * 40)
        
        # Most sustainable
        most_sustainable = max(self.crypto_db.items(), key=lambda x: x[1]['sustainability_score'])
        print(f"🌱 Most Sustainable: {most_sustainable[0]} (Score: {most_sustainable[1]['sustainability_score']}/10)")
        
        # Highest growth potential
        growth_scores = {"very_high": 4, "high": 3, "moderate": 2, "low": 1}
        highest_growth = max(self.crypto_db.items(), key=lambda x: growth_scores.get(x[1]['growth_potential'], 1))
        print(f"🚀 Highest Growth: {highest_growth[0]} ({highest_growth[1]['growth_potential'].replace('_', ' ').title()})")
        
        # Best balanced (sustainability + growth)
        balanced_scores = []
        for coin, data in self.crypto_db.items():
            balance_score = data['sustainability_score'] + growth_scores.get(data['growth_potential'], 1) * 2
            balanced_scores.append((coin, balance_score))
        best_balanced = max(balanced_scores, key=lambda x: x[1])
        print(f"⚖️  Best Balanced: {best_balanced[0]} (Sustainability + Growth)")
        
        print("=" * 80)

    def normalize_query(self, query):
        """Clean and normalize user input"""
        return query.lower().strip()

    def find_sustainable_coins(self):
        """Find coins with high sustainability scores"""
        sustainable_coins = []
        for coin, data in self.crypto_db.items():
            if data["sustainability_score"] >= 7:
                sustainable_coins.append((coin, data["sustainability_score"]))
        
        # Sort by sustainability score (highest first)
        sustainable_coins.sort(key=lambda x: x[1], reverse=True)
        return sustainable_coins

    def find_trending_coins(self):
        """Find coins with rising price trends"""
        trending_coins = []
        for coin, data in self.crypto_db.items():
            if data["price_trend"] == "rising":
                trending_coins.append(coin)
        return trending_coins

    def find_profitable_coins(self):
        """Find coins with high profitability potential"""
        profitable_coins = []
        growth_scores = {"very_high": 4, "high": 3, "moderate": 2, "low": 1}
        
        for coin, data in self.crypto_db.items():
            score = 0
            if data["price_trend"] == "rising":
                score += 2
            if data["market_cap"] == "high":
                score += 1
            score += growth_scores.get(data["growth_potential"], 1)
            
            profitable_coins.append((coin, score))
        
        # Sort by profitability score (highest first)
        profitable_coins.sort(key=lambda x: x[1], reverse=True)
        return profitable_coins

    def get_coin_details(self, coin_name):
        """Get detailed information about a specific coin"""
        for coin, data in self.crypto_db.items():
            if coin.lower() == coin_name.lower() or data["symbol"].lower() == coin_name.lower():
                return coin, data
        return None, None

    def analyze_query(self, query):
        """Analyze user query and determine intent"""
        query = self.normalize_query(query)
        
        # Define keyword patterns
        summary_keywords = ["summary", "all coins", "all crypto", "overview", "list all", "show all", "detailed summary", "full summary", "complete list", "confused","help" ]
        sustainable_keywords = ["sustainable", "eco", "green", "environment", "clean", "carbon"]
        trending_keywords = ["trending", "rising", "hot", "pumping", "growing", "up"]
        profitable_keywords = ["profit", "money", "rich", "gain", "invest", "buy", "best", "millionaire", "million"]
        long_term_keywords = ["long term", "future", "hold", "hodl", "years"]
        specific_coin_keywords = ["bitcoin", "btc", "ethereum", "eth", "cardano", "ada", "solana", "sol", "polygon", "matic", "chainlink", "link"]

        # Check for summary queries first
        if any(keyword in query for keyword in summary_keywords):
            return "summary", None

        # Check for specific coin queries
        for keyword in specific_coin_keywords:
            if keyword in query:
                return "specific_coin", keyword

        # Check for sustainability queries
        if any(keyword in query for keyword in sustainable_keywords):
            return "sustainable", None

        # Check for trending queries
        if any(keyword in query for keyword in trending_keywords):
            return "trending", None

        # Check for profitability queries
        if any(keyword in query for keyword in profitable_keywords):
            return "profitable", None

        # Check for long-term queries
        if any(keyword in query for keyword in long_term_keywords):
            return "long_term", None

        return "general", None

    def generate_response(self, query):
        """Generate appropriate response based on query analysis"""
        intent, specific = self.analyze_query(query)
        
        if intent == "summary":
            self.display_detailed_summary()
            return "Hope this detailed overview helps you make informed decisions! 📊✨"
        
        elif intent == "sustainable":
            sustainable_coins = self.find_sustainable_coins()
            if sustainable_coins:
                top_coin = sustainable_coins[0]
                coin_data = self.crypto_db[top_coin[0]]
                response = f"🌱 For sustainability, I recommend {top_coin[0]} ({coin_data['symbol']})!\n"
                response += f"   • Sustainability Score: {top_coin[1]}/10\n"
                response += f"   • Energy Use: {coin_data['energy_use']}\n"
                response += f"   • Current Price: {coin_data['current_price']}\n"
                response += f"   • It's eco-friendly and has great long-term potential! 🚀"
                
                if len(sustainable_coins) > 1:
                    response += f"\n\n   Other green options: {', '.join([coin[0] for coin in sustainable_coins[1:3]])}"
            else:
                response = "🤔 I couldn't find highly sustainable options in my database right now."

        elif intent == "trending":
            trending_coins = self.find_trending_coins()
            if trending_coins:
                response = f"📈 Hot and trending right now: {', '.join(trending_coins[:3])}!\n"
                for coin in trending_coins[:2]:
                    coin_data = self.crypto_db[coin]
                    response += f"\n   • {coin} ({coin_data['symbol']}): {coin_data['current_price']} - {coin_data['growth_potential']} growth potential"
                response += "\n\n🔥 These coins are showing strong upward momentum!"
            else:
                response = "🤷‍♂️ No clear trending patterns in my current data."

        elif intent == "profitable":
            profitable_coins = self.find_profitable_coins()
            if profitable_coins:
                top_coin = profitable_coins[0][0]
                coin_data = self.crypto_db[top_coin]
                response = f"💰 For maximum profit potential, consider {top_coin} ({coin_data['symbol']})!\n"
                response += f"   • Current Price: {coin_data['current_price']}\n"
                response += f"   • Growth Potential: {coin_data['growth_potential']}\n"
                response += f"   • Market Cap: {coin_data['market_cap']}\n"
                response += f"   • Price Trend: {coin_data['price_trend']} 📊"
                
                response += f"\n\n   Other profitable picks: {', '.join([coin[0] for coin, score in profitable_coins[1:3]])}"
            else:
                response = "📉 Market conditions are mixed right now."

        elif intent == "specific_coin":
            coin_name, coin_data = self.get_coin_details(specific)
            if coin_data:
                response = f"📊 {coin_name} ({coin_data['symbol']}) Analysis:\n"
                response += f"   • Price: {coin_data['current_price']}\n"
                response += f"   • Trend: {coin_data['price_trend']} {'📈' if coin_data['price_trend'] == 'rising' else '📊'}\n"
                response += f"   • Market Cap: {coin_data['market_cap']}\n"
                response += f"   • Growth Potential: {coin_data['growth_potential']}\n"
                response += f"   • Sustainability: {coin_data['sustainability_score']}/10 {'🌱' if coin_data['sustainability_score'] >= 7 else '⚡'}\n"
                response += f"   • Adoption Level: {coin_data['adoption']}"
                
                if coin_data['sustainability_score'] >= 7:
                    response += "\n\n🌿 This is an eco-friendly choice!"
                if coin_data['price_trend'] == 'rising':
                    response += "\n📈 Currently showing positive momentum!"
            else:
                response = f"🤔 I don't have data on '{specific}' in my database. Try Bitcoin, Ethereum, Cardano, Solana, Polygon, or Chainlink!"

        elif intent == "long_term":
            # recommend based on sustainability + growth potential
            long_term_picks = []
            for coin, data in self.crypto_db.items():
                score = data['sustainability_score'] + (3 if data['growth_potential'] == 'high' else 2 if data['growth_potential'] == 'moderate' else 1)
                long_term_picks.append((coin, score))
            
            long_term_picks.sort(key=lambda x: x[1], reverse=True)
            top_pick = long_term_picks[0][0]
            coin_data = self.crypto_db[top_pick]
            
            response = f"🎯 For long-term holding, I recommend {top_pick} ({coin_data['symbol']})!\n"
            response += f"   • Sustainable (Score: {coin_data['sustainability_score']}/10)\n"
            response += f"   • Strong growth potential: {coin_data['growth_potential']}\n"
            response += f"   • Current entry point: {coin_data['current_price']}\n"
            response += f"\n   Other solid long-term picks: {', '.join([coin[0] for coin, score in long_term_picks[1:3]])}"

        else:
            # General response
            responses = [
                "🚀 Ready to explore? Ask me about Bitcoin, Ethereum, Cardano, what's hot in the market, or type 'summary' for a detailed overview!",
                "📈 I'm here to help! What's your crypto goal - quick gains, long-term growth, eco-friendly investing, or want to see all coins summary?"
            ]
            response = random.choice(responses)

        # Add disclaimer
        if intent != "summary":
            response += f"\n\n{random.choice(self.disclaimers)}"
        return response

    def chat(self):
        """Main chat loop"""
        self.greet()
        
        while True:
            try:
                user_input = input(f"\n💬 You: ").strip()
                
                if not user_input:
                    continue
                    
                if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                    print(f"\n🤖 {self.name}: Thanks for chatting! May your crypto journey be profitable and green! Eitah!! 🚀💚")
                    print("=" * 60)
                    break
                
                # Generate and display response
                response = self.generate_response(user_input)
                print(f"\n🤖 {self.name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n\n🤖 {self.name}: Goodbye! Happy trading! 👋")
                break
            except Exception as e:
                print(f"\n🤖 {self.name}: Oops! Something went wrong. Let's try again! 🔄")


def get_market_summary(crypto_db):
    """Generate a market summary"""
    rising_count = sum(1 for data in crypto_db.values() if data['price_trend'] == 'rising')
    stable_count = sum(1 for data in crypto_db.values() if data['price_trend'] == 'stable')
    high_sustainable = sum(1 for data in crypto_db.values() if data['sustainability_score'] >= 7)
    
    print("📊 MARKET SUMMARY")
    print("-" * 30)
    print(f"📈 Rising: {rising_count} coins")
    print(f"📊 Stable: {stable_count} coins") 
    print(f"🌱 Eco-friendly (7+ sustainability): {high_sustainable} coins")
    print("-" * 30)

if __name__ == "__main__":
    chatbot = EzeCrypto()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('message')
    response = chatbot.generate_response(user_input)
    return jsonify({'response': response})

@app.route('/full_summary')
def full_summary():
    return jsonify(chatbot.display_detailed_summary())

if __name__ == '__main__':
    app.run(debug=True)