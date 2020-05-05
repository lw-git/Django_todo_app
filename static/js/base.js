$(document).ready(function () {
	$('.update').on('click', function(e) {
		$('#update').attr('value', 1)
		$('#delete').attr('value', '')
		$('#pk').attr('value', e.target.id.slice(5))
		$('#id_title')[0].value = $('#' + e.target.id)[0].innerText
		if ($('#' + e.target.id).hasClass('completed')){
			$('#id_completed')[0].checked = true
		}
		else{
			$('#id_completed')[0].checked = false
		}	
		$('#id_title')[0].focus()
		$('#submit')[0].value = 'Update'
	});
	$('.close').on('click', function(e) {
		$('#delete').attr('value', 1)
		$('#update').attr('value', '')
		$('#pk').attr('value', e.target.id)
		$('#id_title')[0].value = $('#' + e.target.id)[0].innerText
		$('#submit')[0].click()
	});
});
