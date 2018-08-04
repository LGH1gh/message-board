<template>
    <ul>
        <li v-for='n in this.totalNumber'>
            <board :MID='n' :NUID='1'></board>
        </li>
    </ul>
</template>

<script>
import board from './board'
export default {
    name: 'pageData',
    data: function () {  
        return {
            totalNumber: 0,
            NUID: 0
        }
    },
    components: {
        board
    },
    mounted() {
        this.get_totalNumber()
    },
    methods: {
        get_totalNumber() {
            console.log(this.NUID)
            this.$http.get('http://192.168.55.33:8000/api/get_totalNumber')
                .then((response) => {
                    let res = response.data
                    if (res.error_num == 0) {
                        this.totalNumber = res.total
                        console.log(this.totalNumber)
                    } else {
                        console.log(res.msg)
                    }
                })
        },
        get_params() {
            this.NUID = this.$route.params.NUID
        },
    },
    watch: {
        '$route': 'get_params'
    }
}
</script>

<style scoped>

</style>
