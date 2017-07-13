$(function()
{
	$('.navigation>ul>li').eq(0).addClass('active');
    $('.navigation>ul>li').each(function()
    {
	    var index=$(this).index();
	    $(this).hover(function()
	    {
	    	$(this).addClass('active').siblings().removeClass('active');
	  		$('.container>li').eq(index).stop(true).show().siblings().stop(true).hide();
    	})
    });
	var count=0;
	var len=$(".container>li").length;
	//右边点击按钮
	function btnright() {
		if(count==len-1){
		    count=0;
		}else{
		    count++;
		}
		$('.navigation>ul>li').eq(count).addClass('active').siblings().removeClass('active');
		$('.container>li').eq(count).stop(true).show().siblings().stop(true).hide();
	}
	// 自动播放功能
	var timer=null;
	function aut()
	{
		btnright();
	}
	timer=setInterval(aut,3000);
});