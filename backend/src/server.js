const express = require('express');
const app = express();
app.use(express.json());

app.get('/health', (req, res) => res.json({status:'ok', app:'AgentPost'}));
app.post('/scrape', (req,res)=>res.json({scraped:true}));
app.post('/draft', (req,res)=>res.json({draft_id:1}));
app.post('/approve', (req,res)=>res.json({approved:true}));

app.listen(3000, () => console.log('AgentPost backend on 3000'));
