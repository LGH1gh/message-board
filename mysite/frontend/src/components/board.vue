<template>
    <boardHead UID='UID' time='time' title='title' message='message'></boardHead>
    <boardFoot MID='MID' UID='UID'></boardFoot>
    <comment MID='MID'></comment>
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
            message: ''
        }
    },
    created() {
        console.log('board')
        console.log(this.MID)
    },
    mounted: function() {
        this.get_board(this.MID)
    },
    props: {
        MID: {
            type: Number,
            default: 0
        }
    },
    methods: {
        get_board(MID) {
            this.$http.get('http://192.168.55.33:8000/api/get_board', {params: {MID: MID}})
                .then((response) => {
                    let res = JSON.parse(response.bodyText)
                    console.log(res)
                    if (res.error_num == 0) {
                        this.UID = Number(res['UID'])
                        this.time = res['time']
                        this.title = res['title']
                        this.message = res['message']
                    } else {
                        console.log(res['msg'])
                    }
                })
        }
    }
}
</script>

<style scoped>

</style>
