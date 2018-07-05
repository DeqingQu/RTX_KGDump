document.addEventListener('DOMContentLoaded', init);

function init() {
	getXrayResults();
	getGammaResults();
}

function getXrayResults() {
	var payload = {
			"bypass_cache": "false",
			"known_query_type_id": "Q3",
			"max_results": 100,
			"original_question": "What proteins does IBUPROFEN target?",
			"restated_question": "What proteins are the target of IBUPROFEN",
			"terms": {
				"chemical_substance": "CHEMBL521",
				"rel_type": "directly_interacts_with",
				"target_label": "protein"
			}
		};
	$.ajax({
	            type: "post",
	            url:"http://rtx.ncats.io/api/rtx/v1/query",
	            async: true,
				contentType: "application/json",
	            dataType: "json",
	            data: JSON.stringify(payload),
	            success: function(data) {
					$("#XrayResults").text(JSON.stringify(data));
	            },
	            error: function(XMLHttpRequest, textStatus, errorThrown) {
	                console.log(XMLHttpRequest.status);
	                console.log(XMLHttpRequest.readyState);
	                console.log(textStatus);
	            }
	        });
}


function getGammaResults() {
	var payload = {
            "bypass_cache": "true",
            "known_query_type_id": "Q3",
            "terms": {
                "chemical_substance": "CHEMBL:CHEMBL521"
            },
            "max_results": 100,
            "original_question": "What proteins does IBUPROFEN target?",
            "restated_question": "What proteins are the target of IBUPROFEN"
        };
	$.ajax({
	            type: "post",
	            url:"http://robokop.renci.org:6011/api/query",
	            async: true,
				contentType: "application/json",
	            dataType: "json",
	            data: JSON.stringify(payload),
	            success: function(data) {
					$("#GammaResults").text(JSON.stringify(data));
	            },
	            error: function(XMLHttpRequest, textStatus, errorThrown) {
	                console.log(XMLHttpRequest.status);
	                console.log(XMLHttpRequest.readyState);
	                console.log(textStatus);
	            }
	        });
}
