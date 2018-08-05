<template>
    <div class = 'board'>
        <boardHead :UID='UID' :time='time' :title='title' :message='message'></boardHead>
        <boardFoot :MID='MID' :UID='NUID'>hello</boardFoot>
        <comment :MID='MID' :SUID='NUID'></comment>
    </div>
</template>

<script>
import boardHead from './boardHead'
import boardFoot from './boardFoot'
import comment from './comment'
export default {
    components: {
        boardHead,
        boardFoot,
        comment
    },
    name: 'board',
    data: function() {
        return {
            UID: 0,
            time: '',
            title: '',
            message: '',
        }
    },
    mounted: function() {
        this.get_board(this.MID)
    },
    props: {
        MID: {
            type: Number,
            default: 0
        },
        NUID: {
            type: Number,
            default: 0
        }
    },
    methods: {
        get_board(MID) {
            this.$http.get('http://localhost:8000/api/get_board', {params: {MID: MID}})
                .then((response) => {
                    // console.log(MID)
                    let res = response.data
                    if (res.error_num == 0) {
                        this.UID = res.UID
                        // console.log(this.UID)
                        this.time = res.time
                        this.title = res.title
                        this.message = res.message
                    } else {
                        console.log(res.msg)
                    }
                })
        },
    }
}
</script>

<style scoped>
.board {
    background-color: beige;
    margin-bottom: 100px;
    padding-bottom: 20px;
    padding-top: 20px;
    width: 500px;
    margin-left: auto;
    margin-right: auto;
}
</style>
