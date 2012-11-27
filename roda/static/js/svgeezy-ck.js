/*
* SVGeezy.js 1.0
*
* Copyright 2012, Ben Howdle http://twostepmedia.co.uk
* Released under the WTFPL license
* http://sam.zoy.org/wtfpl/
*
* Date: Sun Aug 26 20:38 2012 GMT
*//*
	//call like so, pass in a class name that you don't want it to check and a filetype to replace .svg with
	svgeezy.init('nocheck', 'png');
*/var svgeezy=function(){return{init:function(e,t){this.avoid=e||"";this.filetype=t||"png";this.svgSupport=this.supportsSvg();if(!this.svgSupport){this.images=document.getElementsByTagName("img");this.imgL=this.images.length;this.fallbacks()}},fallbacks:function(){while(this.imgL--)if(!this.hasClass(this.images[this.imgL],this.avoid)){var e=this.images[this.imgL].getAttribute("src");if(e===null)continue;if(this.getFileExt(e)=="svg"){var t=e.replace(".svg","."+this.filetype);this.images[this.imgL].setAttribute("src",t)}}},getFileExt:function(e){return e.split(".").pop()},hasClass:function(e,t){return(" "+e.className+" ").indexOf(" "+t+" ")>-1},supportsSvg:function(){return document.createElementNS&&document.createElementNS("http://www.w3.org/2000/svg","svg").createSVGRect}}}();