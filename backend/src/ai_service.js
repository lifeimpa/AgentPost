const axios = require('axios');
async function generateContent(prompt, apiKey, provider='openai') {
  // Call OpenAI/Claude/DeepSeek based on config
  return { caption: 'AI generated draft', angles: 3 };
}
module.exports = { generateContent };
