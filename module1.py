import asyncio  # Used for asynchronous programming (non-blocking tasks)

# This class simulates an AI model
class AIModel:
    def predict(self, data):
        # This function processes input data and returns result
        return f"Processed {data}"

# This class simulates a server handling requests
class Server:
    def __init__(self):
        # Create an object of AIModel
        self.model = AIModel()

    async def process(self, data):
        # Simulate delay (like network or computation time)
        await asyncio.sleep(1)

        # Call AI model to process data
        return self.model.predict(data)

# Main async function
async def main():
    server = Server()  # Create server object

    # Call async process function and wait for result
    result = await server.process("input data")

    # Print the result
    print(result)

# Run the async program
asyncio.run(main())