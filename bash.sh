for file in *txt

do
 	grep -v "^[[:space:]]" $file | tr -d "\r" >tempfile
	sed ’/^\s*$/d’ tempfile
	sed -r 's/[A-Z]*[A-Z]/abbreviation/g' $file >tempfile	
mv tempfile $file

done 

