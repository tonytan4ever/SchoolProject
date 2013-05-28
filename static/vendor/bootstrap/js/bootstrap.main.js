require([
         "dijit/layout/BorderContainer",
         "dijit/layout/ContentPane",
         "dijit/layout/TabContainer",
         "dijit/form/TextBox",
         "dijit/form/Button",
         "dojo/domReady!"
     ], function(BorderContainer, ContentPane, TabContainer, TextBox, Button){
         // create a BorderContainer as the top widget in the hierarchy
         var bc_main = new BorderContainer({style: "height: 100%; width: 100%;"});

         // create a ContentPane as the left pane in the BorderContainer
         var bc_header = new BorderContainer({
             region: "top",
             style: "height: 10%",
         });
         
         var cp_header_left = new ContentPane({
         	region: "left",
         	style : "width: 30%",
         	content : "Left"
         })
         
          var cp_header_middle = new ContentPane({
         	region: "center",
         	style : "width: 50%",
         })
         
          var cp_header_right = new ContentPane({
         	region: "right",
         	//style : "width: 35%",
         })

         bc_header.addChild(cp_header_left);
         
         cp_header_middle.addChild(new TextBox({
         	name: "Post Search Box",
       		value: "" /* no or empty value! */,
        	placeHolder: "Type in your search term"
         }));        
         cp_header_middle.addChild(new Button({
         	label: "Search",
         }));
         
         
         bc_header.addChild(cp_header_middle);
         
         
         cp_header_right.addChild(new Button({
         	label: "Login",
         }))
         bc_header.addChild(cp_header_right);
         
         bc_main.addChild(bc_header);

         // create a TabContainer as the center pane in the BorderContainer,
         // which itself contains two children
         var tc = new TabContainer({region: "center"});
         var tab1 = new ContentPane({title: "Home",
        	               content: "Home content"
         }),
         tab2 = new ContentPane({title: "Get Tutoring",
                           content: "All Posts"
         }),
         tab3 = new ContentPane({title: "Get Paid",
                   		  content: "Getting paid here"
         });
         tc.addChild( tab1 );
         tc.addChild( tab2 );
         tc.addChild( tab3 );
         bc_main.addChild(tc);

         // put the top level widget into the document, and then call startup()
         document.body.appendChild(bc_main.domNode);
         bc_main.startup();
     });