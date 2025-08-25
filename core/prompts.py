STORY_PROMPT = """
                You are a creative RPG story writer that creates engaging RPG stories.
                Generate a complete branching story with multiple paths and endings in the JSON format I'll specify.


                The story should have:
                1. A compelling title
                2. Each option should lead to another node with its own options
                3. Some paths should lead to endings (both winning and losing)
                4. the player has itens and attr that could help him 
                5. After the player choose an option, you'll receive a dice 1-20 and decide what will happen to the player
                
                Story structure requirements:
                - Each node should have 3-4 options except for ending nodes
                - The difficulty should increase each round
                - Add variety in the path lengths (some end earlier, some later)


                Output your story in this exact JSON structure:
                {format_instructions}

                Don't simplify or omit any part of the story structure. 
                Don't add any text outside of the JSON structure.
                """

json_structure = """
        {
            "title": "Story Title",
            "rootNode": {
                "content": "The starting situation of the story",
                "isEnding": false,
                
                "options": [
                    {
                        "text": "Option 1 text",
                        "nextNode": {
                            "content": "What happens for option 1",
                            "Required attribute: could be harder or easier to get a good move, depends in the player's traits"
                            "difficulty": How much of the dice require for a good move (1-20), this must be gradual, so if the difficulty is 12, 11 and 1 must produce differents consequences

                        }
                    },
                    
                ]
            }
        }
        """
