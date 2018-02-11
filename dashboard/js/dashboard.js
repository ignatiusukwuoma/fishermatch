$(function(){
    var knew = $('#new');
    var trending = $('#trending');
    var popular = $('#popular');
    var dashboard = $('#dashboard');
    var researchers = $('#researchers');
    var fishers = $('#fishers');
    $('#dash').click(function(){
        researchers.attr('hidden', 'hidden');
        fishers.attr('hidden', 'hidden');
        dashboard.removeAttr('hidden');
    });
    $('#knew').click(function(){
        trending.attr('hidden','hidden');
        popular.attr('hidden', 'hidden');
        knew.removeAttr('hidden');
    });
    $('#trend').click(function(){
        knew.attr('hidden','hidden');
        popular.attr('hidden', 'hidden');
        trending.removeAttr('hidden');
    });
    $('#pop').click(function(){
        knew.attr('hidden','hidden');
        trending.attr('hidden', 'hidden');
        popular.removeAttr('hidden');
    });
    $('#research').click(function(){
        dashboard.attr('hidden', 'hidden');
        fishers.attr('hidden', 'hidden');
        researchers.removeAttr('hidden');
    });
    $('#fish').click(function(){
        researchers.attr('hidden', 'hidden');
        dashboard.attr('hidden', 'hidden');
        fishers.removeAttr('hidden');
    });
});