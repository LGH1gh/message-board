<template>
    <div class='board-foot'>
        <div>
            <div v-if='amAgree == 1' class='fa fa-thumbs-up'>
                {{ agreeNumber }} 
            </div>
            <div v-else class='fa fa-thumbs-o-up'>
               {{ agreeNumber }} 
            </div>
        </div>
        <div>
           <div v-if='amAgree == -1' class='fa fa-thumbs-down'>
                {{ disagreeNumber }} 
            </div>
            <div v-else class='fa-thumbs-o-down'>
                {{ disagreeNumber }} 
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'boardFoot',
    data: function() {
        return {
            amAgree: 0, 
            agreeNumber: 0,
            disagreeNumber: 0
        }
    },
    props: {
        MID: {
            type: Number,
            default: 0
        },
        UID: {
            type: Number,
            default: 0
        }
    },
    mounted: function() {
        this.get_agreeNumber(this.MID)
        this.get_disagreeNumber(this.MID)
        this.get_amAgree(this.MID)
        // console.log(MID)
    },
    methods: {
        get_agreeNumber(MID) {
            this.$http.get('http://192.168.55.33:8000/api/get_agreeNumber', {params: {MID: MID}})
                .then((response) => {
                    let res = response.data
                    // console.log(res)
                    if (res.error_num == 0) {
                        this.agreeNumber = Number(res.agreeNumber)
                    } else {
                        console.log(res.msg)
                    }
                })
        },
        get_disagreeNumber(MID) {
            this.$http.get('http://192.168.55.33:8000/api/get_disagreeNumber', {params: {MID: MID}})
                .then((response) => {
                    let res = response.data
                    // console.log(res)
                    if (res.error_num == 0) {
                        this.agreeNumber = Number(res.disagreeNumber)
                    } else {
                        console.log(res.msg)
                    }
                })
        },
        get_amAgree(MID) {
            this.$http.get('http://192.168.55.33:8000/api/get_amAgree', {params: {MID: MID}})
                .then((response) => {
                    let res = response.data
                    // console.log(res)
                    if (res.error_num == 0) {
                        this.agreeNumber = Number(res.amAgree)
                    } else {
                        console.log(res.msg)
                    }
                })
        }
    }
}
</script>

<style scoped>

</style>
