<template>
    <div class="biz-content">
        <div class="biz-top-bar">
            <div class="dashboard-top-title">
                gamedeployments
            </div>
            <dashboard-top-actions />
        </div>
        <div class="biz-content-wrapper">
            gamedeployments
        </div>
    </div>
</template>
<script>
    import { defineComponent, ref } from '@vue/composition-api'
    import DashboardTopActions from '../common/dashboard-top-actions'

    export default defineComponent({
        name: 'HelloWorld',
        components: { DashboardTopActions },
        props: {
            msg: {
                type: String,
                required: true
            }
        },
        setup () {
            const count = ref(0)

            const addCount = () => {
                count.value = count.value + 1
            }
            return {
                count,
                addCount
            }
        }
    })

</script>
<style scoped>
    @import './gamedeployments.css';
</style>
