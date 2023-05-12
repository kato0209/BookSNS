const BookRegistrationApp=Vue.createApp({
    data:()=>({
      reserve_book_url:"/register-reserved-book/",
      finish_book_url:"/register-finished-book/",
    }),
    methods:{
        register_reserved_book:function(event){
          const headers={
              'X-Requested-With': 'XMLHttpRequest',
              'Content-Type':'application / json',
              'X-CSRFToken':event.currentTarget.dataset.csrfToken,
          }
          let data={
            "ISBNcode":event.currentTarget.dataset.isbncode,
          }
          data=JSON.stringify(data)
          axios.post(this.reserve_book_url,data,{headers:headers})
          .then(function(res){
            const target_buttons=document.getElementsByName('reserve_book_'+res.data.ISBNcode);
            if(res.data.reserved){
              for(let button of target_buttons){
                button.classList.add('active')
              }
            }else{
              for(let button of target_buttons){
                button.classList.remove('active')
              }
            }
          })
          .catch(function(error){
            console.log(error)
          })
        },
        register_finished_book:function(event){
          const headers={
              'X-Requested-With': 'XMLHttpRequest',
              'Content-Type':'application / json',
              'X-CSRFToken':event.currentTarget.dataset.csrfToken,
          }
          let data={
            "ISBNcode":event.currentTarget.dataset.isbncode,
          }
          data=JSON.stringify(data)
          axios.post(this.finish_book_url,data,{headers:headers})
          .then(function(res){
            const target_buttons=document.getElementsByName('finish_book_'+res.data.ISBNcode);
            if(res.data.finished){
              for(let button of target_buttons){
                button.classList.add('active')
              }
            }else{
              for(let button of target_buttons){
                button.classList.remove('active')
              }
            }
          })
          .catch(function(error){
            console.log(error)
          })
        }
    }
})
BookRegistrationApp.config.compilerOptions.delimiters = ['[[', ']]']