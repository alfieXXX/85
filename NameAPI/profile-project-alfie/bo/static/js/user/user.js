$(document).ready(function(){
	var User = {
		Init: function(config) {
			this.config = config;
			this.BindEvents();
		},
        BindEvents: function() {
			let $this = this.config;

                $this.btn_search.on('click',{param: 1} ,this.Search );
                $this.btn_new.on('click',{param: 1} ,this.ShowModal );
                $this.btn_save.on('click',{param: 1} ,this.Save );
                $this.tbl_user.on('click','.btn-edit',{param: 2} ,this.ShowModal );
		},
        Save: (e, data) => {
            let $route  = (typeof e === 'object') ? e.data.param : e;
			let $self = User.config;

            switch($route){
                case 1:
                        // alert(e.target.getAttribute('data-action'))                    
                        let $formdata = $self.modal_form_user.serializeArray();
                        let $method_type = '', $url = '/bo/user/save/';

                        if(e.target.getAttribute('data-action') === 'update'){
                            $formdata.push({name:'userid',value: e.target.getAttribute('data-userid')})
                            $method_type = 'PUT';
                            $url += `${e.target.getAttribute('data-userid')}/`;
                        }else{
                            $method_type = 'POST';
                        }
                        console.log($formdata);
                        $payload = {url : $url, method_type : $method_type, payload : User.objectifyForm($formdata)}

                        const $common = new Common($payload)
                        
                        $common.ApiData()
                        .then(data => console.log(data))
                        .catch(err => {
                            console.log('err',err)
                        })                        
                break;
            }

        },
        objectifyForm: (formArray) => {
            //serialize data function
            var returnArray = {};
            for (var i = 0; i < formArray.length; i++){
                returnArray[formArray[i]['name']] = formArray[i]['value'];
            }
            return returnArray;
        },       
        ShowModal: (e, data) => {
            let $route  = (typeof e === 'object') ? e.data.param : e;
			let $self = User.config;
            
            switch($route){
                case 1:// user new entry
                        $self.btn_save.attr('data-action','new');
                        $self.modal_user.find('.modal-title').text('New User');
                        $self.modal_user.modal('show');
                break;
                case 2:// update user
                        $self.btn_save.attr('data-userid',e.target.getAttribute('data-userid'));
                        $self.btn_save.attr('data-action','update');
                        $self.modal_form_user.find('[name=firstname]').val( e.target.getAttribute('data-firstname') );
                        $self.modal_user.find('.modal-title').text('Update User');
                        $self.modal_user.modal('show');
                break;                
            }
        },
        Search: (e, data) => {
            let $route  = (typeof e === 'object') ? e.data.param : e;
			let $self = User.config;

            switch($route){
                case 1: 
                        let $params = new URLSearchParams();

                        $params.append('search_value', $self.form_search.find('[name=search-value]').val().trim());                          
                        $params.append('firstname', 'momo');                          
                        $params.append('lastname', 'papo');                          
                        let $url_param = '/bo/user/list/?' + $params;    				
            //http://127.0.0.1:8080/bo/user/list/?search_value=aaa
                        $payload = {url : $url_param,method_type : 'GET'}
            
                        const $common = new Common($payload)
            
                        $common.ApiData()
                        .then(data => {
                            User.Search(2, data);
                            
                        })
                        .catch(err => {
                            console.log('err',err)
                        })                  
                break;
                case 2: 
                        if(data.code != 200){
                            alert(data.message);
                            return;
                        }

                        let $users = data.data, $txt = '';

                        $self.tbl_user.empty(); 

                        $users.forEach($row => {
                            $txt += `
                                    <tr id="${ $row.user_id }">  
                                        <td scope="col">${ $row.firstname }</td>
                                        <td scope="col" colspan="2">${ $row.lastname }</td>
                                        <td scope="col" >
                                            <button 
                                                    class="btn btn-outline-info btn-edit" 
                                                    type="button" 
                                                    data-userid="${ $row.user_id }"
                                                    data-firstname="${ $row.firstname }"
                                            >Edit</button>
                                        </td>
                                    </tr>                              
                            `;
                                
                                
                        });
                
                        $self.tbl_user.append($txt); 
                break;
            }
        },
	 
	}

	User.Init({
         tbl_user        : $('#tbl-user')
        ,form_search     : $('#form-search')
        ,modal_user      : $('#modal-user')
        ,modal_form_user : $('#modal-form-user')
        ,btn_new         : $('.btn-new')
        ,btn_search      : $('.btn-search')
        ,btn_save        : $('.btn-save')

    })    

})