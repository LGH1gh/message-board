<template>
    <div>
        <div class="note" :style ="note"></div>
        <h3>登录</h3>
        <form @submit.prevent='get_UID'>
            <div>
                <label for='username'>用户名:</label>
                <input type='text' id='username' name='username' v-model='username' required>
            </div>
            <div>
                <label for='username'>密码:  </label>
                <input type='password' id='password' name='password' v-model='password' required>
            </div>
            <div v-if='this.isLogin == false'>你输入的帐号或密码不正确，请重新输入。</div>
            <input type='submit' value='提交'>
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
            isLogin: true,
            UID: 0,
            note: {
                backgroundImage: "url(" + require("../assets/bg.png") + ")",
                backgroundRepeat: "no-repeat",
                backgroundSize: "25px auto",
                marginTop: "5px",
            }
        }
    },
    methods: {
        get_UID() {
            this.$http.get('http://192.168.55.33:8000/api/get_UID', {params: {username: this.username, password: this.password}})
                .then((response)  => {
                    let res = response.data
                    if (res.error_num == 0) {
                        this.UID = Number(res.UID)
                        this.isLogin = true
                        this.$router.push({
                            name: 'pageData' ,
                            params: {
                                NUID: this.UID
                            }
                            })
                    } else {
                        console.log(res.msg)
                        this.isLogin = false
                    }
                })
        }
    }
}
</script>

<style scoped>

</style>
