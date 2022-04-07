$(document).ready(function(){
	var Signup = {
		Init: function(config) {
			this.config = config;
			this.BindEvents();
		},
        BindEvents: function() {
			let $this = this.config;

                $this.btn_save.on('click', this.ClickMe );
		},

        ClickMe: () => {
			let $self = Signup.config;
			let $data = {
				'firstname' : $self.fname.val(),
				'lastname' : $self.lname.val(),
				'email' : $self.email.val(),
				'username' : $self.username.val(),
				'password' : $self.password.val(),
				// 'Confirm Password':$self.confirm_pass.val()
			}
			// console.log($data); 
			// return;
			$payload = {
				url : '/save/'
			   ,method_type : 'POST'
			   ,payload : $data
		    }
		
		   const $common = new Common($payload)
		
		   $common.ApiData()
		   .then(data => console.log(data))
		   .catch(err => {
			   console.log('err',err)
		   })


        },
	 
	}

	Signup.Init({
        btn_save 		: $('#btn-save')
        ,fname 			: $('#fname')
        ,lname 			: $('#lname')
        ,email			: $('#email')
        ,username		: $('#username')
        ,password		: $('#password')
		,confirm_pass	: $('#confirm-pass')
    })    

})