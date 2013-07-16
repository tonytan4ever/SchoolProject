require([
    "dojo/_base/declare",
    "dojo/_base/lang",
    "dojo/on",
    "dojo/dom",
    "dojo/Evented",
    "dojo/_base/Deferred",
    "dojo/json",
    
    "dijit/_Widget",
    "dijit/_TemplatedMixin",
    "dijit/_WidgetsInTemplateMixin",
    
    "dijit/Dialog",
    "dijit/form/Form",
    "dijit/form/ValidationTextBox",
    "dijit/form/Button",
    
    "dojo/domReady!"
], function(
    declare,
    lang,
    on,
    dom,
    Evented,
    Deferred,
    JSON,
        
    _Widget,
    _TemplatedMixin, 
    _WidgetsInTemplateMixin,
        
     Dialog
) {

    var LoginDialog = declare([Dialog, Evented], {
        
        READY: 0,
        BUSY: 1,
        
        title: "Login Dialog",
        message: "",
        busyLabel: "Working...",
        
        // Binding property values to DOM nodes in templates
        // see: http://www.enterprisedojo.com/2010/10/02/lessons-in-widgetry-binding-property-values-to-dom-nodes-in-templates/
        attributeMap: lang.delegate(dijit._Widget.prototype.attributeMap, {
            message: {
                node: "messageNode",
                type: "innerHTML"               
            }            
        }),
        
        constructor: function(/*Object*/ kwArgs) {
            lang.mixin(this, kwArgs);            
            var dialogTemplate = dom.byId("dialog-template").textContent; 
            var formTemplate = dom.byId("login-form-template").textContent;
            var template = lang.replace(dialogTemplate, {
                form: formTemplate                
            });

            var contentWidget = new (declare(
                [_Widget, _TemplatedMixin, _WidgetsInTemplateMixin],
                {
                    templateString: template                   
                }
            )); 
            contentWidget.startup();
            var content = this.content = contentWidget;
            this.form = content.form;
            // shortcuts
            this.submitButton = content.submitButton;
            this.cancelButton = content.cancelButton;
            this.messageNode = content.messageNode;
        },
        
        postCreate: function() {
            this.inherited(arguments);
            
            this.readyState= this.READY;
            this.okLabel = this.submitButton.get("label");
            
            this.connect(this.submitButton, "onClick", "onSubmit");
            this.connect(this.cancelButton, "onClick", "onCancel");
            
            this.watch("readyState", lang.hitch(this, "_onReadyStateChange"));
            
            this.form.watch("state", lang.hitch(this, "_onValidStateChange"));
            this._onValidStateChange();
        },
        
        onSubmit: function() {
            this.set("readyState", this.BUSY);
            this.set("message", ""); 
            var data = this.form.get("value");
            
            var auth = this.controller.login(data);
            
            Deferred.when(auth, lang.hitch(this, function(loginSuccess) {
                if (loginSuccess === true) {
                    this.onLoginSuccess();
                    return;                    
                }
                this.onLoginError();
            }));
        },
            
        onLoginSuccess: function() {
            this.set("readyState", this.READY);
            this.set("message", "Login sucessful.");             
            this.emit("success");
        },
        
        onLoginError: function() {
            this.set("readyState", this.READY);
            this.set("message", "Please try again."); 
            this.emit("error");         
        },
        
        onCancel: function() {
           this.emit("cancel");     
        },

        _onValidStateChange: function() {
            this.submitButton.set("disabled", !!this.form.get("state").length);
        },

        _onReadyStateChange: function() {
            var isBusy = this.get("readyState") == this.BUSY;
            this.submitButton.set("label", isBusy ? this.busyLabel : this.okLabel);
            this.submitButton.set("disabled", isBusy);
        }            
    });
    
    var LoginController = declare(null, {
    
        constructor: function(kwArgs) {
            lang.mixin(this, kwArgs);
        },
        
        login: function(data) {
            // simulate calling web service for authentication
            var def = new Deferred();
            setTimeout(lang.hitch(this, function() {
                def.resolve(data.username == this.username && data.password == this.password);                
            }), 1000);
            return def;
        }
    });

    // provide username & password in constructor
    // since we do not have web service here to authenticate against    
    /*var loginController = new LoginController({username: "user", password: "user"});
    
    var loginDialog = new LoginDialog({ controller: loginController});
    loginDialog.startup();
    loginDialog.show();
    
    loginDialog.on("cancel", function() {
        console.log("Login cancelled.");        
    });
    
    loginDialog.on("error", function() { 
        console.log("Login error.");
    });
    
    loginDialog.on("success", function() { 
        console.log("Login success.");
        console.log(JSON.stringify(this.form.get("value")));
    });*/     
});