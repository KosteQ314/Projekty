x=1

read -p "How many pushups would you like to do?: "
while [[ $x -le $y ]]
do
    read -p "Pushup $x: Press enter to continue"
    (( x ++ ))
done
echo "Congrats, you completed your pushups!"