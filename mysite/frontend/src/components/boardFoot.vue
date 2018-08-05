<template>
    <div class='board-foot'>
        <div class='agree'>
            <div v-if='amAgree == 1' style='width: 20px'>
                <button @click='re_agree'>
                    <v-icon name='thumbs-up' class='choose'></v-icon>
                    {{ agreeNumber }}
                </button>
            </div>

            <div v-else style='width: 20px'>
                <button @click='add_agree'>
                    <v-icon name='thumbs-up'></v-icon>
                    {{ agreeNumber }} 
                </button>
            </div>
        </div>
        <div class='agree'>
           <div v-if='amAgree == -1' style='width: 20px'>
                <button @click='re_agree'>
                    <v-icon name='thumbs-down' class='choose'></v-icon>
                    {{ disagreeNumber }} 
                </button>
            </div>
            <div v-else style='width: 20px'>
                <button @click='add_disagree'>
                    <v-icon name='thumbs-down'></v-icon>
                    {{ disagreeNumber }} 
                </button>
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
        this.get_agreeNumber()
        this.get_disagreeNumber()
        this.get_amAgree()
        // console.log(MID)
    },
    methods: {
        get_agreeNumber() {
            this.$http.get('http://localhost:8000/api/get_agreeNumber', {params: {MID: this.MID}})
                .then((response) => {
                    let res = response.data
                    // console.log(res)
                    if (res.error_num == 0) {
                        // console.log(res)
                        this.agreeNumber = Number(res.agreeNumber)
                    } else {
                        console.log(res.msg)
                    }
                })
        },
        get_disagreeNumber() {
            this.$http.get('http://localhost:8000/api/get_disagreeNumber', {params: {MID: this.MID}})
                .then((response) => {
                    let res = response.data
                    // console.log(res)
                    if (res.error_num == 0) {
                        // console.log(res)
                        this.disagreeNumber = Number(res.disagreeNumber)
                    } else {
                        console.log(res.msg)
                    }
                })
        },
        get_amAgree() {
            // console.log(this.MID)
            // console.log(this.UID)
            this.$http.get('http://localhost:8000/api/get_amAgree', {params: {MID: this.MID, UID: this.UID}})
                .then((response) => {
                    let res = response.data
                    // console.log(res)
                    if (res.error_num == 0) {
                        // console.log(res)
                        this.amAgree = Number(res.amAgree)
                    } else {
                        console.log(res.msg)
                    }
                })
        },
        re_agree() {
            this.$http.get('http://localhost:8000/api/add_agree', {params: {MID: this.MID, UID: this.UID, agree: 0}})
                .then((response) => {
                    let res = response.data
                    if (res.error_num == 0) {
                        // console.log(res)
                        this.get_agreeNumber()
                        this.get_disagreeNumber()
                        this.get_amAgree()
                    } else {
                        console.log(res.msg)
                    }
                })
        },
        add_agree() {
            this.$http.get('http://localhost:8000/api/add_agree', {params: {MID: this.MID, UID: this.UID, agree: 1}})
                .then((response) => {
                    let res = response.data
                    if (res.error_num == 0) {
                        // console.log(res)
                        this.get_agreeNumber()
                        this.get_disagreeNumber()
                        this.get_amAgree()
                    } else {
                        console.log(res.msg)
                    }
                })
        },
        add_disagree() {
            this.$http.get('http://localhost:8000/api/add_agree', {params: {MID: this.MID, UID: this.UID, agree: -1}})
                .then((response) => {
                    let res = response.data
                    if (res.error_num == 0) {
                        // console.log(res)
                        this.get_agreeNumber()
                        this.get_disagreeNumber()
                        this.get_amAgree()
                        // console.log(this.amAgree)
                    } else {
                        console.log(res.msg)
                    }
                })
        },
    }
}
</script>

<style scoped>
.choose {
    color: rgb(255, 0, 0);
}
.board-foot {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
</style>
