/**
 * This file is referenced by the `dojoBuild` key in `package.json` and provides extra hinting specific to the Dojo
 * build system about how certain files in the package need to be handled at build time. Build profiles for the
 * application itself are stored in the `profiles` directory.
 */

var profile = (function(){
    return {
        basePath: "./",
        releaseDir: "./",
        releaseName: "release",
        action: "release",
        
        cssOptimize: true,
 
        packages: [
                   
           { name: "dojo", location: "./dojo-release-1.9.1-src/dojo" },
           { name: "dijit",location: "./dojo-release-1.9.1-src/dijit"},
           { name: "dojox",location: "./dojo-release-1.9.1-src/dojox"},

            // internal JS classes

            // LGF templates(LXML files)
            //{ name: "lgf", location: "lgf/" },
        ],
 
        layers: {
            "dojo/dojo": {
                include: [ 
					"dijit/layout/BorderContainer",
					"dijit/layout/ContentPane",
					"dijit/layout/TabContainer",
					"dijit/form/TextBox",
					"dijit/form/Button",
                    "dojo/domReady"		
		    ],
                customBase: true,
                boot: true
            },
            //"framework/Dialog": {
            //    include: [ "app/Dialog" ]
            //}
        }
    };
})();

