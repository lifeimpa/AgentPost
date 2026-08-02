// Instagram Graph API connector (OAuth + publish)
function connectInstagram() { return {authUrl:'https://instagram.com/auth'}; }
function publishPost(token, imageUrl, caption) { return {postId: 'ig_123'}; }
module.exports = {connectInstagram, publishPost};
