<template>
    <div class='login'>
        <div class='title'>
            <h3>账号密码登录</h3>
        </div>
        <form class='login_form'>
            <div>
                <label for='username'>用户名:</label>
                <input type='text' id='username' name='username' v-model='username' required>
            </div>
            <div>
                <label for='username'>密码:  </label>
                <input type='password' id='password' name='password' v-model='password' required>
            </div>
            <div v-if='this.isLogin == 0' class='holder'></div>
            <div v-if='this.isLogin == -1' class='text'>你输入的帐号或密码不正确，请重新输入。</div>
            <div v-if='this.isLogin == -2' class='text'>你所注册的用户名已被占用，请重新输入。</div>
            <input type='submit' value='登录' class='submit' @click='get_UID'>
            <input type='submit' value='注册' class='register' @click='add_user'>
        </form>
    </div>
</template>

<script>
export default {
    name: 'login',
    data: function() {
        return {
            username: '',
            password: '',
            isLogin: 0,
            UID: 0
        }
    },
    methods: {
        get_UID() {
            this.$http.get('http://localhost:8000/api/get_UID', {params: {username: this.username, password: this.password}})
                .then((response)  => {
                    let res = response.data
                    if (res.error_num == 0) {
                        this.UID = Number(res.UID)
                        this.isLogin = 0
                        sessionStorage.setItem('user', this.UID)
                        this.$router.push({
                            name: 'pageData' ,
                            params: {
                                NUID: this.UID
                            }
                            })
                    } else {
                        console.log(res.msg)
                        this.isLogin = -1
                    }
                })
        },
        add_user() {
            this.$http.get('http://localhost:8000/api/add_user', {params: {username: this.username, password: this.password}})
                .then((response) => {
                    let res = response.data
                    if (res.error_num == 0) {
                        this.UID = this.get_UID(this.username)
                        console.log(this.UID)
                        this.isLogin = 0
                        sessionStorage.setItem('user', this.UID)
                        this.$router.push({
                            name: 'pageData',
                            params: {
                                NUID: this.UID
                            }
                        })
                    } else {
                        this.isLogin = -2
                        console.log(res.msg)
                    }
                })
        }
    }
}
</script>

<style scoped>

</style>
