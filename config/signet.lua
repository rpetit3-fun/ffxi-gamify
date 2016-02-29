---------------------------------------------------------------------------------------------------
-- func: signet
-- desc: Apply earned buffs to player.
---------------------------------------------------------------------------------------------------

cmdprops =
{
    permission = 0,
    parameters = ""
};

function onTrigger(player)
    if (player:getVar("Signet++") == 0) then
        -- on
        player:setVar("Signet++", 1);
        player:addStatusEffect(EFFECT_SIGNET,0,0,3600*24); -- Grant Signet
        player:addMod(MOD_HPP, player:getVar("[SIGNET]HP_Boost") * 3);
        player:addMod(MOD_MPP, player:getVar("[SIGNET]MP_Boost") * 3);
        player:addMod(MOD_DEFP, player:getVar("[SIGNET]Defense") * 5);
        player:addMod(MOD_EVAP, player:getVar("[SIGNET]Evasion") * 5);
        player:addMod(MOD_ATTP, player:getVar("[SIGNET]Attack") * 5);
        player:addMod(MOD_REGEN, player:getVar("[SIGNET]Regen"));
        player:addMod(MOD_REFRESH, player:getVar("[SIGNET]Refresh"));
        player:addMod(MOD_REGAIN, player:getVar("[SIGNET]Regain") * 3);
        player:addStatusEffect(EFFECT_DEDICATION,1000,0,86400,0,30000);
    else
        -- off
        player:setVar("Signet++", 0);
        player:delStatusEffect(EFFECT_SIGNET);
        player:delMod(MOD_HPP, player:getVar("[SIGNET]HP_Boost") * 3);
        player:delMod(MOD_MPP, player:getVar("[SIGNET]MP_Boost") * 3);
        player:delMod(MOD_DEFP, player:getVar("[SIGNET]Defense") * 5);
        player:delMod(MOD_EVAP, player:getVar("[SIGNET]Evasion") * 5);
        player:delMod(MOD_ATTP, player:getVar("[SIGNET]Attack") * 5);
        player:delMod(MOD_REGEN, player:getVar("[SIGNET]Regen"));
        player:delMod(MOD_REFRESH, player:getVar("[SIGNET]Refresh"));
        player:delMod(MOD_REGAIN, player:getVar("[SIGNET]Regain") * 3);
        player:delStatusEffect(EFFECT_DEDICATION);
    end
end
