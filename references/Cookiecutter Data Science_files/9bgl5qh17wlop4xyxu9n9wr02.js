!function(){function e(e,t){e.parentNode.insertBefore(t,e.nextSibling)}function t(e,t){function i(e){var i=t.getAttribute("data-"+e);return i?e+"="+i:void 0}var a=["size","speed","autoplay","loop","theme","t","preload"];return"?"+a.map(i).filter(Boolean).join("&")}function i(e){var t=document.createElement("a");return t.href=e,t}function a(e){var t=i(e.src);return t.protocol+"//"+t.host}function n(i){function n(e){if(e.origin===l){var t=e.data[0],i=e.data[1],a=o.contentWindow||o;e.source==a&&"asciicast:size"==t&&(o.style.width=""+i.width+"px",o.style.height=""+i.height+"px")}}if(!i.dataset.player){var l=a(i),r=i.id.split("-")[1],s=document.createElement("div");s.id="asciicast-container-"+r,s.className="asciicast",s.style.display="block",s.style.float="none",s.style.overflow="hidden",s.style.padding=0,s.style.margin="20px 0",e(i,s);var o=document.createElement("iframe");o.src=l+"/a/"+r+"/embed"+t(s,i),o.id="asciicast-iframe-"+r,o.name="asciicast-iframe-"+r,o.scrolling="no",o.setAttribute("allowFullScreen","true"),o.style.overflow="hidden",o.style.margin=0,o.style.border=0,o.style.display="inline-block",o.style.width="100%",o.style.float="none",o.style.visibility="hidden",o.onload=function(){this.style.visibility="visible"},s.appendChild(o),window.addEventListener("message",n,!1),i.dataset.player=s}}var l=document.querySelectorAll("script[id^='asciicast-']");[].forEach.call(l,n)}();