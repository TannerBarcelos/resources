import { ChatOpenAI } from "@langchain/openai";

const llm = new ChatOpenAI({
    apiKey: process.env.OPENAI_API_KEY,
    modelName: "gpt-4-1106-preview",
});

const llmResponse = await llm.invoke("What is the capital of France?");
console.log(llmResponse);