// Approval + Schedule logic
function approveDraft(draftId, edit) { return {approved:true, draftId}; }
function schedulePost(draftId, time, platform) { return {scheduled:true}; }
module.exports = {approveDraft, schedulePost};
